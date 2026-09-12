/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 11:56:21 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/06 08:01:13 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	validnum(char *str)
{
	int		it;
	long	num;

	it = 0;
	if (str[it] == '+' || str[it] == '-')
		it++;
	if (!str[it])
		return (0);
	while (str[it])
	{
		if (str[it] < '0' || str[it] > '9')
			return (0);
		it++;
	}
	num = ft_atoi(str);
	if (num > 2147483647 || num < -2147483648)
		return (0);
	return (1);
}

int	can_2add_if(t_stack *stack_a, char *str)
{
	int		num;
	t_node	*temp;
	int		it;

	it = 0;
	num = 0;
	if (validnum(str))
		num = (int)ft_atoi(str);
	else
		return (num);
	temp = stack_a->head;
	while (it < stack_a->size)
	{
		if (temp->val == num)
			return (0);
		it++;
		temp = temp->next;
	}
	add_node(stack_a, num);
	return (1);
}

int	check_config(char *str)
{
	int	lenth;

	lenth = len(str);
	if (lenth == 7 && ft_strncmp("--bench", str, lenth) == 0)
		return (4);
	else if (lenth == 8 && ft_strncmp("--simple", str, lenth) == 0)
		return (0);
	else if (lenth == 8 && ft_strncmp("--medium", str, lenth) == 0)
		return (1);
	else if (lenth == 9 && ft_strncmp("--complex", str, lenth) == 0)
		return (2);
	else if (lenth == 10 && ft_strncmp("--adaptive", str, lenth) == 0)
		return (3);
	return (-1);
}

t_stack	*parser(int argc, char **argv, t_config *conf, t_stack *stack_a)
{
	int		it;
	char	*str;

	it = 1;
	while (it < argc)
	{
		str = argv[it];
		if (str[0] == '-' && str[1] == '-')
		{
			if (check_config(str) == -1)
				return (NULL);
			else if (check_config(str) == 4)
				conf->bench = 1;
			else
				conf->mod = check_config(str);
		}
		else
		{
			if (can_2add_if(stack_a, str) == 0)
				return (NULL);
		}
		it++;
	}
	return (stack_a);
}

int	main(int argc, char **argv)
{
	t_config	conf;
	t_stack		*stack_a;

	conf.mod = 3;
	conf.bench = 0;
	stack_a = stack_create();
	if (parser(argc, argv, &conf, stack_a) == NULL)
	{
		clear_stack(stack_a);
		write(2, "Error\n", 6);
		return (0);
	}
	if (compute_disorder(stack_a) == 0.0)
	{
		clear_stack(stack_a);
		return (0);
	}
	start_sort(stack_a, &conf);
	return (0);
}
