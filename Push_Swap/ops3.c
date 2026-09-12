/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops3.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 09:42:26 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/05 09:42:26 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_node	*case_one(t_stack *from)
{
	t_node	*temp;

	if (from->size == 1)
	{
		temp = from->head;
		from->head = NULL;
	}
	else
	{
		temp = from->head;
		from->head->prev->next = from->head->next;
		from->head->next->prev = from->head->prev;
		from->head = from->head->next;
	}
	return (temp);
}

void	px(t_stack *from, t_stack *to)
{
	t_node	*temp;

	if (!from || !to || !from->head)
		return ;
	if (from->size < 1)
		return ;
	temp = case_one(from);
	if (to->size == 0)
	{
		to->head = temp;
		to->head->next = to->head;
		to->head->prev = to->head;
	}
	else
	{
		temp->next = to->head;
		temp->prev = to->head->prev;
		to->head->prev->next = temp;
		to->head->prev = temp;
		to->head = temp;
	}
	from->size -= 1;
	to->size += 1;
	to->px += 1;
}
