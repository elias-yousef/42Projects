/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 15:43:30 by mkhashan          #+#    #+#             */
/*   Updated: 2026/01/29 15:43:30 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	d(t_stack *stack_x, int val)
{
	t_node	*temp;
	int		f_d;
	int		b_d;

	f_d = 0;
	b_d = 0;
	temp = stack_x->head;
	while (temp->val != val)
	{
		temp = temp->next;
		f_d += 1;
	}
	temp = stack_x->head;
	while (temp->val != val)
	{
		temp = temp->prev;
		b_d -= 1;
	}
	if (-1 * b_d > f_d)
		return (f_d);
	else
		return (b_d);
}

int	is_sorted(t_stack *a)
{
	t_node	*temp;

	if (!a || !a->head)
		return (1);
	temp = a->head;
	while (temp->next)
	{
		if (temp->val > temp->next->val)
			return (0);
		temp = temp->next;
	}
	return (1);
}

void	a_1s(void (*f)(t_stack *), t_stack *stack_x, char *ops, int times)
{
	while (times)
	{
		f(stack_x);
		write(1, ops, len(ops));
		write(1, "\n", 1);
		times--;
	}
}

void	a_2s(t_stack *f, t_stack *t, char *ops, int n)
{
	while (n--)
	{
		if (ops[0] == 'p')
			px(f, t);
		else if (ft_strncmp("rrr", ops, 3) == 0)
			rrr(f, t);
		else if (ops[0] == 's')
			ss(f, t);
		else
			rr(f, t);
		write(1, ops, len(ops));
		write(1, "\n", 1);
	}
}
